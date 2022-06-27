from django.test import TestCase
from django.utils.datastructures import MultiValueDictKeyError
import tempfile
from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import (
    Case, Motherboard,
    Cpu, Gpu, Ram,
    Psu, Storage
)
from .models import (
    Order,
    OrderLineCase, OrderLineMotherboard,
    OrderLineCpu, OrderLineGpu, OrderLineRam,
    OrderLinePsu, OrderLineStorage
)
import datetime

class TestViews(TestCase):

    def setUp(self):
        """
        setUp function to create objects
        """
        self.test_case = Case.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price=123,
            mobo_sizes='micro_atx',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.test_motherboard = Motherboard.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price=50,
            size='micro_atx',
            socket='1200',
            ram_type='ddr4',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.test_cpu = Cpu.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price=123,
            socket='1200',
            core_count=8,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.test_gpu = Gpu.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price=123,
            speed='2200',
            memory_capacity=8,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.test_ram = Ram.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price = 123,
            speed=3200,
            capacity=16,
            type='ddr4',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.test_psu = Psu.objects.create(
            model = 'test_model',
            manufacturer = 'test_manufacturer',
            description = 'test_description',
            price = 123,
            wattage=700,
            e_category='80plus_gold',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.test_storage = Storage.objects.create(
            model = 'test_model',
            manufacturer = 'test_manufacturer',
            description = 'test_description',
            price = 123,
            capacity=500,
            speed=3500,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.normal_user = User.objects.create(username='testuser', email='test@email.com')
        self.normal_user.set_password('test_password')
        self.normal_user.save()
        self.admin = User.objects.create_superuser(username='testadmin', email='test@email.com')
        self.admin.set_password('test_password')
        self.admin.save()

    def test_checkout_get(self):
        """Test checkout page GET request"""
        self.client.login(username='testuser', password='test_password')
        test_profile = UserProfile.objects.get(
            user=self.normal_user,
        )
        test_profile.profile_city = 'Athens'
        test_profile.save()
        session = self.client.session
        session['bag'] = {}
        session['bag']['case_1'] = 1
        session.save()
        response = self.client.get('/checkout/', follow=True)
        session['bag'] = {}
        session.save()
        response = self.client.get('/checkout/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('checkout/checkout.html')

    def test_checkout_post(self):
        """Test checkout page POST request"""
        test_profile = UserProfile.objects.get(
            user=self.normal_user,
        )
        test_profile.profile_city = 'Athens'
        test_profile.save()
        self.client.login(username='testuser', password='test_password')
        session = self.client.session
        session['bag'] = {}
        session['bag']['case_1'] = 1
        session['bag']['motherboard_1'] = 1
        session['bag']['cpu_1'] = 1
        session['bag']['gpu_1'] = 1
        session['bag']['ram_1'] = 1
        session['bag']['psu_1'] = 1
        session['bag']['storage_1'] = 1
        session.save()
        response = self.client.post('/checkout/', {
            'full_name': 'test_name',
            'email': 'test_email@email.com',
            'phone_number': 1234567,
            'country': 'GR',
            'postcode': 12345,
            'city': 'Athens',
            'street_address1': 'test_address',
            'street_address2': 'test_address2',
            'client_secret': 'client_secret_key',
            'save-info': 'true',
        }, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_checkout_bad_post(self):
        """Test checkout page bad POST request"""
        session = self.client.session
        session['bag'] = {}
        session['bag']['cpu_4'] = 1
        session.save()
        with self.assertRaises(Cpu.DoesNotExist):
            response = self.client.post('/checkout/', {
                'full_name': 'test_name',
                'email': 'test_email@email.com',
                'phone_number': 1234567,
                'country': 'GR',
                'postcode': 12345,
                'city': 'Athens',
                'street_address1': 'test_address',
                'street_address2': 'test_address2',
                'client_secret': 'client_secret_key',
                'save-info': 'true',
            }, follow=True)

    def test_checkout_success_get(self):
        """Test checkout success GET with bad data"""
        test_order = Order.objects.create(
            user=self.normal_user,
            full_name='test_name',
            email='test_email',
            phone_number=123456,
            country='GR',
            postcode=12345,
            city='Athens',
            street_address1='test_address',
            date=datetime.date.today(),
        )
        test_lineitem = OrderLineCase.objects.create(
            quantity=1,
            product=self.test_case,
            order=test_order,
        )
        test_order.save()
        test_lineitem.save()
        response = self.client.get(f'/checkout/checkout_success/{test_order.order_number}')
        self.assertEqual(response.status_code, 200)

    def test_cache_checkout_data(self):
        """Test cache checkout data function"""
        session = self.client.session
        session['bag'] = {}
        session['bag']['case_1'] = 1
        session['bag']['motherboard_1'] = 1
        session['bag']['cpu_1'] = 1
        session['bag']['gpu_1'] = 1
        session['bag']['ram_1'] = 1
        session['bag']['psu_1'] = 1
        session['bag']['storage_1'] = 1
        session.save()
        response = self.client.post('/checkout/cache_checkout_data/', {
            'full_name': 'test_name',
            'email': 'test_email@email.com',
            'phone_number': 1234567,
            'country': 'GR',
            'postcode': 12345,
            'city': 'Athens',
            'street_address1': 'test_address',
            'street_address2': 'test_address2',
            'client_secret': 'client_secret_key',
            'save-info': 'true',
        }, follow=True)
        self.assertEqual(response.status_code, 400)
