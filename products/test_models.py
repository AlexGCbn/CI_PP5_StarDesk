from django.test import TestCase
from django.contrib.auth.models import User
from .models import (
    Case, Motherboard,
    Cpu, Gpu, Ram,
    Psu, Storage
)
import datetime


class TestModels(TestCase):

    def setUp(self):
        """
        setUp function to create objects
        """
        test_case = Case.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price=123,
            mobo_sizes='micro_atx',
        )
        test_motherboard = Motherboard.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price=123,
            size='micro_atx',
            socket='1200',
            ram_type='ddr4',
        )
        test_cpu = Cpu.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price=123,
            socket='1200',
            core_count=8
        )
        test_gpu = Gpu.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price=123,
            speed='2200',
            memory_capacity=8,
        )
        test_ram = Ram.objects.create(
            model='test_model',
            manufacturer='test_manufacturer',
            description='test_description',
            price = 123,
            speed=3200,
            capacity=16,
            type='ddr4',
        )
        test_psu = Psu.objects.create(
            model = 'test_model',
            manufacturer = 'test_manufacturer',
            description = 'test_description',
            price = 123,
            wattage=700,
            e_category='80plus_gold',
        )
        test_storage = Storage.objects.create(
            model = 'test_model',
            manufacturer = 'test_manufacturer',
            description = 'test_description',
            price = 123,
            capacity=500,
            speed=3500,
        )
        test_user = User.objects.create_user(
            username = 'test_user',
            email = 'test_email@email.com',
            password = 'test_password',
        )

    def test_case_defaults(self):
        """Test Case default values"""
        case = Case.objects.get(id=1)
        self.assertEqual(case.category, 'case')

    def test_motherboard_defaults(self):
        """Test Motherboard default values"""
        motherboard = Motherboard.objects.get(id=1)
        self.assertEqual(motherboard.category, 'motherboard')

    def test_cpu_defaults(self):
        """Test Cpu default values"""
        cpu = Cpu.objects.get(id=1)
        self.assertEqual(cpu.category, 'cpu')

    def test_gpu_defaults(self):
        """Test Gpu default values"""
        gpu = Gpu.objects.get(id=1)
        self.assertEqual(gpu.category, 'gpu')

    def test_ram_defaults(self):
        """Test Ram default values"""
        ram = Ram.objects.get(id=1)
        self.assertEqual(ram.category, 'ram')

    def test_psu_defaults(self):
        """Test Psu default values"""
        psu = Psu.objects.get(id=1)
        self.assertEqual(psu.category, 'psu')

    def test_storage_defaults(self):
        """Test Storage default values"""
        storage = Storage.objects.get(id=1)
        self.assertEqual(storage.category, 'storage')
