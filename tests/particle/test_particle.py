from particle.particle.enums import Charge, Par, SpinType
from particle.particle import Particle
from particle.pdgid import PDGID

def test_enums_Charge():
    assert Charge.p + Charge.m == Charge.o
    assert Charge.pp + Charge.mm == Charge.o


def test_enums_SpinType():
    assert SpinType.PseudoScalar == - SpinType.Scalar
    assert SpinType.Axial == - SpinType.Vector
    assert SpinType.PseudoTensor == - SpinType.Tensor


def test_pdg():
    assert Particle.from_pdgid(211).pdgid == 211

def test_pdg_convert():
    p = Particle.from_pdgid(211)
    assert isinstance(p.pdgid, PDGID)
    assert int(p) == 211
    assert PDGID(p) == 211

def test_sorting():
    assert Particle.from_pdgid(211) < Particle.from_pdgid(311)
    assert Particle.from_pdgid(211) < Particle.from_pdgid(-311)

def test_int_compare():
    assert Particle.from_pdgid(211) > 0
    assert Particle.from_pdgid(-211) < 0
    assert Particle.from_pdgid(211) >= 0
    assert Particle.from_pdgid(-211) <= 0

    assert 0 < Particle.from_pdgid(211)
    assert 0 > Particle.from_pdgid(-211)
    assert 0 <= Particle.from_pdgid(211)
    assert 0 >= Particle.from_pdgid(-211)

def test_str():
    pi = Particle.from_pdgid(211)
    assert str(pi) == 'pi+'


def test_rep():
    pi = Particle.from_pdgid(211)
    assert 'pdgid=211' in repr(pi)
    assert "name='pi'" in repr(pi)
    assert 'mass=139.57' in repr(pi)


def test_prop():
    pi = Particle.from_pdgid(211)
    assert pi.name == 'pi'
    assert pi.pdgid == 211
    assert pi.charge == Par.p


def test_ampgen_style_names():
    assert Particle.from_string('pi+').pdgid == 211
    assert Particle.from_string('pi-').pdgid == -211
    assert Particle.from_string('K~*0').pdgid == -313
    assert Particle.from_string('K*(892)bar0').pdgid == -313
    assert Particle.from_string('a(1)(1260)+').pdgid == 20213

    # Direct comparison to integer works too
    assert Particle.from_string('rho(1450)0') == 100113
    assert Particle.from_string('rho(770)0') == 113

    assert Particle.from_string('K(1)(1270)bar-') == -10323
    assert Particle.from_string('K(1460)bar-') == -100321



def test_decfile_style_names():
    assert Particle.from_dec('anti-K*0').pdgid == -313
    assert Particle.from_dec('a_1(1260)+').pdgid == 20213
    #assert Particle.from_dec("D'_1+").pdgid == 7
    #assert Particle.from_dec("D_2*+").pdgid == 8