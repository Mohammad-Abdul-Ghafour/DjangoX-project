from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Employees


class EmployeesTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="admin", email="admin@admin.com", password="12345"
        )

        self.employee = Employees.objects.create(
            name="pickle", position='manager', start_date='2021-12-8',is_active=True,register=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.employee), "pickle")

    def test_thing_content(self):
        self.assertEqual(f"{self.employee.name}", "pickle")
        self.assertEqual(f"{self.employee.register}", "admin")
        self.assertEqual(self.employee.position, "manager")

    def test_thing_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "_employee_base.html")

    def test_thing_detail_view(self):
        response = self.client.get(reverse("employee_details", args="1"))
        # no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "admin")
        self.assertTemplateUsed(response, "_employee_base.html")

    def test_thing_create_view(self):
        response = self.client.post(
            reverse("create_employee"),
            {
                "name": "Rake",
                "position": "manager",
                "start_date": "2021-12-8",
                "is_active":"True",
                "register":self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("employee_details", args="2"))
        self.assertContains(response, "Rake")

    def test_thing_update_view_redirect(self):
        response = self.client.post(
            reverse("update_employee", args="1"),
            {"Name": "qwer","Register":self.user.id}
        )

        self.assertRedirects(response, reverse("employee_details",args="1"))

    def test_thing_delete_view(self):
        response = self.client.get(reverse("delete_employee", args="1"))
        self.assertEqual(response.status_code, 200)