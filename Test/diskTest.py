import unittest
from Code.disk import Disk
from Code.program import Program

class TestsDisk(unittest.TestCase):

    def setUp(self):
        self.disk= Disk()

    def test_when_write_program_toDisk_Then_verify_that_the_program_list_is_incremented(self):
        program= Program()
        self.disk.writeProgram(program)
        self.assertEqual(len(self.disk.programs), 1)

    def test_when_write_program_toDisk_Then_verify_that_obtain_the_program(self):
        program= Program()
        self.disk.writeProgram(program)
        self.assertEqual(self.disk.getProgram("program0"), program)

