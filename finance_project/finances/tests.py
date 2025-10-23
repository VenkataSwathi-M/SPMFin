from django.test import TestCase
from .models import Expense

class ExpenseModelTest(TestCase):
    def test_create_expense(self):
        exp = Expense.objects.create(name="Food", amount=200)
        self.assertEqual(exp.amount, 200)
