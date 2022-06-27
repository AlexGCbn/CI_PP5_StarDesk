from django.test import TestCase
import tempfile
from django.contrib.auth.models import User
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
        self.normal_user = User.objects.create(username='testuser', email='test@email.com')
        self.normal_user.set_password('test_password')
        self.normal_user.save()
        self.admin = User.objects.create_superuser(username='testadmin', email='test@email.com')
        self.admin.set_password('test_password')
        self.admin.save()


    def test_uuid_and_str(self):
        """Test Order UUID creation"""
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
        order_str = str(test_order)
        self.assertEqual(order_str, test_order.order_number)
        lineitem_str = str(test_lineitem)
        self.assertEqual(lineitem_str, 'Order item test_manufacturer test_model')

    def test_delivery_threshold(self):
        """Test delivery threshold for orders"""
        
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
        test_lineitem = OrderLineMotherboard.objects.create(
            quantity=1,
            product=self.test_motherboard,
            order=test_order,
        )
        test_order.save()
        test_lineitem.save()
        test_order.update_total()
        self.assertEqual(test_order.delivery_cost, 3.5)
