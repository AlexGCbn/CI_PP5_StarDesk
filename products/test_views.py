from django.test import TestCase
import tempfile
from django.contrib.auth.models import User
from .models import (
    Case, Motherboard,
    Cpu, Gpu, Ram,
    Psu, Storage
)
from .forms import (
    CaseForm, MotherboardForm,
    CpuForm, GpuForm, RamForm,
    PsuForm, StorageForm
)
from reviews.models import CaseReview
import datetime


# Image solution found here:
# https://stackoverflow.com/a/32814129/17822071

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
            price=123,
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
            price=123,
            speed=3200,
            capacity=16,
            type='ddr4',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.test_psu = Psu.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price=123,
            wattage=700,
            e_category='80plus_gold',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.test_storage = Storage.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price=123,
            capacity=500,
            speed=3500,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.normal_user = User.objects.create(
            username='testuser',
            email='test@email.com'
        )
        self.normal_user.set_password('test_password')
        self.normal_user.save()
        self.admin = User.objects.create_superuser(
            username='testadmin',
            email='test@email.com'
        )
        self.admin.set_password('test_password')
        self.admin.save()

    def test_get_all_products(self):
        """
        Test all products GET
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_products_with_categories(self):
        """
        Test all products GET
        """
        response = self.client.get('/products/?category=case')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/?category=motherboard')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/?category=cpu')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/?category=gpu')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/?category=ram')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/?category=psu')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/?category=storage')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_products_with_search_query(self):
        """
        Test GET products with search query
        """
        response = self.client.get('/products/?q=corsair')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/?q=')
        self.assertRedirects(response, '/products/')

    def test_get_products_with_sorting(self):
        """
        Test GET products with sorting
        """
        response = self.client.get('/products/?sort=price&direction=asc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/?sort=price&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_details(self):
        """Test product details view for all categories"""
        response = self.client.get('/products/case/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')
        response = self.client.get('/products/motherboard/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')
        response = self.client.get('/products/cpu/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')
        response = self.client.get('/products/gpu/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')
        response = self.client.get('/products/ram/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')
        response = self.client.get('/products/psu/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')
        response = self.client.get('/products/storage/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')

    def test_product_reviewed(self):
        """Test product reviewed by user"""
        user = self.normal_user
        self.test_review = CaseReview.objects.create(
            product=self.test_case,
            user=user,
            score=4,
            comment='test_comment',
        )
        self.client.login(username='testuser', password='test_password')
        response = self.client.get('/products/case/1/')
        self.assertEqual(response.status_code, 200)

    def test_add_product_to_bag(self):
        """Test adding product to bag"""
        session = self.client.session
        session['bag'] = {}
        session['bag']['case_1'] = 1
        session.save()
        response = self.client.post('/products/case/1/', {
            'quantity': 2,
            'redirect_url': '/products/case/1/'
        })
        self.assertRedirects(response, '/products/case/1/')
        response = self.client.post('/products/motherboard/1/', {
            'quantity': 2,
            'redirect_url': '/products/motherboard/1/'
            })
        self.assertRedirects(response, '/products/motherboard/1/')

    def test_admin_add_product_get(self):
        """Test admin add product GET request"""
        self.client.login(username='testadmin', password='test_password')
        response = self.client.get('/products/add_product/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')
        self.client.logout()
        self.client.login(username='testuser', password='test_password')
        response = self.client.get('/products/add_product/', follow=True)
        self.assertRedirects(response, '/products/')

    def test_admin_add_case_post(self):
        """Test admin add case POST request"""
        self.client.login(username='testadmin', password='test_password')
        response = self.client.post('/products/add_product/', {
            'category': 'case',
            'model': 'test_model2',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'mobo_sizes': 'atx',
        }, follow=True)

        new_product = Case.objects.get(id=2)
        self.assertEqual(new_product.model, 'test_model2')

        response = self.client.post('/products/add_product/', {
            'category': 'case',
            'model': 'test_model2',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
        }, follow=True)
        self.assertRedirects(response, '/products/add_product/')

        self.client.logout()
        self.client.login(username='testuser', password='test_password')
        response = self.client.post('/products/add_product/', {
            'category': 'case',
            'model': 'test_model2',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'mobo_sizes': 'atx',
        }, follow=True)
        self.assertRedirects(response, '/products/')

    def test_admin_add_rest_of_products(self):
        """Test admin add product POST request"""
        self.client.login(username='testadmin', password='test_password')
        self.client.post('/products/add_product/', {
            'category': 'motherboard',
            'model': 'test_model2',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'size': 'micro_atx',
            'socket': '1200',
            'ram_type': 'ddr4',
        }, follow=True)
        new_product = Motherboard.objects.get(id=2)
        self.assertEqual(new_product.model, 'test_model2')

        response = self.client.post('/products/add_product/', {
            'category': 'cpu',
            'model': 'test_model2',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'socket': '1200',
            'core_count': 8,
        }, follow=True)
        new_product = Cpu.objects.get(id=2)
        self.assertEqual(new_product.model, 'test_model2')

        response = self.client.post('/products/add_product/', {
            'category': 'gpu',
            'model': 'test_model2',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'speed': '2200',
            'memory_capacity': 8,
        }, follow=True)
        new_product = Gpu.objects.get(id=2)
        self.assertEqual(new_product.model, 'test_model2')

        response = self.client.post('/products/add_product/', {
            'category': 'ram',
            'model': 'test_model2',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'speed': 3200,
            'capacity': 16,
            'type': 'ddr4',
        }, follow=True)
        new_product = Ram.objects.get(id=2)
        self.assertEqual(new_product.model, 'test_model2')

        response = self.client.post('/products/add_product/', {
            'category': 'psu',
            'model': 'test_model2',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'wattage': 700,
            'e_category': '80plus_gold',
        }, follow=True)
        new_product = Psu.objects.get(id=2)
        self.assertEqual(new_product.model, 'test_model2')

        self.client.post('/products/add_product/', {
            'category': 'storage',
            'model': 'test_model2',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'capacity': 500,
            'speed': 3500,
        }, follow=True)
        new_product = Storage.objects.get(id=2)
        self.assertEqual(new_product.model, 'test_model2')

    def test_admin_manage_product_get(self):
        """Test admin manage case GET request"""
        self.client.login(username='testadmin', password='test_password')
        response = self.client.get('/products/case/1/edit/', {
            'category': 'case',
            'id': 1
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

        self.client.logout()
        self.client.login(username='testuser', password='test_password')
        response = self.client.get('/products/case/1/edit/', {
            'category': 'case',
            'id': 1
        }, follow=True)
        self.assertRedirects(response, '/products/')

    def test_admin_manage_product_get_rest(self):
        """Test admin manage products GET request"""
        self.client.login(username='testadmin', password='test_password')
        response = self.client.get('/products/motherboard/1/edit/', {
            'category': 'motherboard',
            'id': 1
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
        response = self.client.get('/products/cpu/1/edit/', {
            'category': 'cpu',
            'id': 1
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
        response = self.client.get('/products/gpu/1/edit/', {
            'category': 'gpu',
            'id': 1
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
        response = self.client.get('/products/ram/1/edit/', {
            'category': 'ram',
            'id': 1
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
        response = self.client.get('/products/psu/1/edit/', {
            'category': 'psu',
            'id': 1
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
        response = self.client.get('/products/storage/1/edit/', {
            'category': 'storage',
            'id': 1
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_admin_manage_product_post(self):
        """Test admin manage case POST request"""
        self.client.login(username='testadmin', password='test_password')
        response = self.client.post('/products/case/1/edit/', {
            'category': 'case',
            'id': 1,
            'model': 'updated_model',
            'manufacturer': 'test_manufacturer',
            'description': 'test_description',
            'price': 123,
            'mobo_sizes': 'micro_atx',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        edited_product = Case.objects.get(id=1)
        self.assertEqual(edited_product.model, 'updated_model')

        self.client.logout()
        self.client.login(username='testuser', password='test_password')
        response = self.client.post('/products/case/1/edit/', {
            'category': 'case',
            'id': 1,
            'model': 'model',
            'manufacturer': 'test_manufacturer',
            'description': 'test_description',
            'price': 123,
            'mobo_sizes': 'micro_atx',
        }, follow=True)
        self.assertRedirects(response, '/products/')
        edited_product = Case.objects.get(id=1)
        self.assertEqual(edited_product.model, 'updated_model')

        self.client.logout()
        self.client.login(username='testadmin', password='test_password')
        response = self.client.post('/products/case/1/delete/', {
            'category': 'case',
            'id': 1,
        }, follow=True)
        cases = Case.objects.all()
        self.assertQuerysetEqual(cases, [])

    def test_admin_manage_product_post_rest(self):
        """Test admin manage products POST request"""
        self.client.login(username='testadmin', password='test_password')
        response = self.client.post('/products/motherboard/1/edit/', {
            'category': 'motherboard',
            'id': 1,
            'model': 'updated_model',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'size': 'micro_atx',
            'socket': '1200',
            'ram_type': 'ddr4',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        edited_product = Motherboard.objects.get(id=1)
        self.assertEqual(edited_product.model, 'updated_model')
        response = self.client.post('/products/cpu/1/edit/', {
            'category': 'cpu',
            'id': 1,
            'model': 'updated_model',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'socket': '1200',
            'core_count': 8,
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        edited_product = Cpu.objects.get(id=1)
        self.assertEqual(edited_product.model, 'updated_model')
        response = self.client.post('/products/gpu/1/edit/', {
            'category': 'gpu',
            'id': 1,
            'model': 'updated_model',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'speed': '2200',
            'memory_capacity': 8,
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        edited_product = Gpu.objects.get(id=1)
        self.assertEqual(edited_product.model, 'updated_model')
        response = self.client.post('/products/ram/1/edit/', {
            'category': 'ram',
            'id': 1,
            'model': 'updated_model',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'speed': 3200,
            'capacity': 16,
            'type': 'ddr4',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        edited_product = Ram.objects.get(id=1)
        self.assertEqual(edited_product.model, 'updated_model')
        response = self.client.post('/products/psu/1/edit/', {
            'category': 'psu',
            'id': 1,
            'model': 'updated_model',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'wattage': 700,
            'e_category': '80plus_gold',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        edited_product = Psu.objects.get(id=1)
        self.assertEqual(edited_product.model, 'updated_model')
        response = self.client.post('/products/storage/1/edit/', {
            'category': 'storage',
            'id': 1,
            'model': 'updated_model',
            'manufacturer': 'test_manufacturer2',
            'description': 'test_description2',
            'price': 123,
            'capacity': 500,
            'speed': 3500,
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        edited_product = Storage.objects.get(id=1)
        self.assertEqual(edited_product.model, 'updated_model')
