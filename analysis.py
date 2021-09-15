from coffea.nanoevents import NanoEventsFactory, DelphesSchema
from coffea import processor, hist
import awkward as ak
import pathlib

class MyJetMass(processor.ProcessorABC):
    def __init__(self):
        self._histo = hist.Hist(
            "Events",
            hist.Cat("dataset", "Dataset"),
            hist.Bin("mass", "leading jet mass [GeV]", 40, 0, 1000),
        )

    @property
    def accumulator(self):
        return self._histo

    # we will receive a NanoEvents instead of a coffea DataFrame
    def process(self, events):
        out = self.accumulator.identity()

        mask = ak.num(events.Jet) > 0
        mmevents = events[mask]
        out.fill(
            dataset=events.metadata["dataset"],
            mass=mmevents.Jet[0].mass,
        )
        return out

    def postprocess(self, accumulator):
        return accumulator

samples = {
    "100TeV_B": list(map(str, pathlib.Path("/collab/project/snowmass21/data/smmc/v0.1/r1/100TeV_B.tar.gz/delphesstep/").glob("*.root")))
}

result = processor.run_uproot_job(
    samples,
    "Delphes",
    MyJetMass(),
    processor.futures_executor,
    {"schema": DelphesSchema, "workers": 16},
)

result.to_hist()['100TeV_B', :].show()
