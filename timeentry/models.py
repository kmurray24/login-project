from django.db import models
from django.db.models import Sum
from phone_field import PhoneField

TRANS_CHOICES = ( 
			("TIME", "Time Entry"), 
			("EXPENSE", "Expense Entry.") ) 

TRANS_STATUS = ( 
			("OPEN", "Open Time Entry.  Not yet submitted"), 
			("SUBMITTED", "Submitted Time Entry.  Waiting for approval"),
			("APPROVED", "Approved Time Entry. Waiting for payment"),
			("PAID", "Paid Time Entry. No further action required") )

# TRANS_STATUS = { "OPEN": "Open Time Entry.  Not yet submitted", 
# 			"SUBMITTED": "Submitted Time Entry.  Waiting for approval",
# 			"APPROVED": "Approved Time Entry. Waiting for payment",
# 			"PAID": "Paid Time Entry. No further action required" }


class Period(models.Model):
	def __str__(self):
		return u'\u00A0 {} \u00A0\u00A0 {}\u00A0\u00A0  to\u00A0\u00A0  {} \u00A0\u00A0\u00A0 {}'.format(self.id, self.begindate, self.enddate, self.notes)

	begindate = models.DateField(verbose_name="Begin Date",)
	enddate   = models.DateField(verbose_name="End Date")
	notes     = models.TextField(("Notes"), blank=True, null=True)


class Case(models.Model):
	
	def __str__(self):
		return u'{}: \u00A0\u00A0 {}\u00A0\u00A0 {}'.format(self.id, self.name, self.notes)
	
	id    = models.AutoField(primary_key=True)
	name  = models.CharField(max_length=40, verbose_name="Name")
	notes =  models.TextField(("Notes"), blank=True, null=True)


class Expert(models.Model):

	def __str__(self):
		return u'{}: \u00A0\u00A0 {} \u00A0\u00A0 {} \u00A0\u00A0 {} \u00A0\u00A0 {}'.format(self.id, self.firstname, self.lastname, self.email, self.phone)

	id        = models.AutoField(primary_key=True)
	firstname = models.CharField(max_length=30, verbose_name="First Name")
	lastname  = models.CharField(max_length=30, verbose_name="Last Name")
	phone     = PhoneField(blank=True, help_text='Contact phone number')
	email     = models.EmailField(max_length=60, verbose_name="Email", blank=True, null=True)
	notes     =  models.TextField(("Notes"), blank=True, null=True)

class Claim(models.Model):

	def __str__(self):
		return u'Claim ID:\u00A0\u00A0{}\u00A0\u00A0  Type:\u00A0\u00A0{}   \u00A0\u00A0|\u00A0\u00A0\u00A0Expert:\u00A0\u00A0{}\u00A0{}   \u00A0\u00A0{}   \u00A0\u00A0{}'.format( self.id, self.type, self.expert.firstname,self.expert.lastname, self.period.begindate, self.case.name)

	expert  = models.ForeignKey(Expert, on_delete=models.CASCADE)
	case    = models.ForeignKey(Case, on_delete=models.CASCADE)
	date    = models.DateField(verbose_name="Date")
	period  = models.ForeignKey(Period, on_delete=models.CASCADE)
	type    = models.CharField(choices = TRANS_CHOICES, max_length=7)
	hours   = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	expense = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
	status  = models.CharField(choices = TRANS_STATUS, max_length=10)
	datetime_input     = models.DateTimeField(null=True, blank=True)
	datetime_submitted = models.DateTimeField(null=True, blank=True)
	datetime_approved  = models.DateTimeField(null=True, blank=True)
	datetime_paid      = models.DateTimeField(null=True, blank=True)
	notes = models.TextField(("Notes"), blank=True, null=True)

	@staticmethod
	def get_claim_summary(self):
		claim_summary = Claim.objects.values('expert', 'case', 'period', 'status').annotate(total_hours=Sum('hours'), total_expense=Sum('expense'))
		return claim_summary