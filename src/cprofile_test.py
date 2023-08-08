"""Profiling test for palingramsfinder."""
import cProfile
import palingramsfinder
cProfile.run('palingramsfinder.find_palingrams()')
