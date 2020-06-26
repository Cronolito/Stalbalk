# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2020-06-26.

from Ver2.start import Beam

def test_sections():
    beamObject = Beam()
    beamObject.add_i_section('sektion1', 300, 10, 280, 8, 350, 12)
    beamObject.add_i_section('sektion2', 400, 10, 280, 8, 450, 12)
    beamObject.beam_definition = [[0,2,4],['sektion1', 'sektion2', 'sektion3']]
    beamObject.generate_sections()
    print(beamObject.main_sections)


test_sections()