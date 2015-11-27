import unittest

from Code.pcb import Pcb


class TestsPcb(unittest.TestCase):
    def setUp(self):
        pass

    def test_when_increment_program_count_then_verify_program_count_is_incremented(self):
        pcb = Pcb(0, 0, 0)
        pcb.incrementPc()
        self.assertEqual(pcb.pc, 1)
        pass
