# Coffea Analysis Example

This repository provides an example analysis script for processing the Delphes outputs produced by the Snowmass MC Prod task force.

## Installation

Using a python3 installation in a virtual environment, e.g.

```
python3 -m venv myenv
source myenv/bin/activate
```

you can install the requirements via

```
python -m pip install -r requirements.txt
```

## Caveats

The following branches are not interpretable by coffea just yet:

  - `Area`
  - `Constituents`
  - `Particle`
  - `Particles`
  - `PrunedP4[5]`
  - `SoftDroppedJet`
  - `SoftDroppedP4[5]`
  - `SoftDroppedSubJet1`
  - `SoftDroppedSubJet2`
  - `TrimmedP4[5]`

But work is on-going, see [coffeateam/coffea#584](https://github.com/CoffeaTeam/coffea/pull/584/).

## Running

Simply run

```
python analysis.py
```

which outputs a histogram using `histoprint`. For one Delphes file, one sees

```
 0.00e+00 _                             4.68e+04 ╷
 2.50e+01 _███████████████████████████████████████
 5.00e+01 _█
 7.50e+01 _
 1.00e+02 _
 1.25e+02 _
 1.50e+02 _
 1.75e+02 _
 2.00e+02 _
 2.25e+02 _
 2.50e+02 _
 2.75e+02 _
 3.00e+02 _
 3.25e+02 _
 3.50e+02 _
 3.75e+02 _
 4.00e+02 _
 4.25e+02 _
 4.50e+02 _
 4.75e+02 _
 5.00e+02 _
 5.25e+02 _
 5.50e+02 _
 5.75e+02 _
 6.00e+02 _
 6.25e+02 _
 6.50e+02 _
 6.75e+02 _
 7.00e+02 _
 7.25e+02 _
 7.50e+02 _
 7.75e+02 _
 8.00e+02 _
 8.25e+02 _
 8.50e+02 _
 8.75e+02 _
 9.00e+02 _
 9.25e+02 _
 9.50e+02 _
 9.75e+02 _
 1.00e+03 _
```

which takes about 2 seconds to run. For all 350+ files in one of the samples, it takes a little over 1 hour with 16 cores:

```
$ time python analysis.py
Preprocessing: 100%|███████████████████████████████████████████████████████████████████████████████| 352/352 [00:33<00:00, 10.44file/s]
Processing:  27%|█████████████████████▉                                                            | 94/352 [17:53<32:03,  7.46s/chunk]Processing: 100%|███████████████████████████████████████████████████████████████████████████████| 352/352 [1:03:01<00:00, 10.74s/chunk]
 0.00e+00 _                                                                                                                 1.20e+03 ╷
 2.50e+01 _███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
 5.00e+01 _██
 7.50e+01 _
 1.00e+02 _
 1.25e+02 _
 1.50e+02 _
 1.75e+02 _
 2.00e+02 _
 2.25e+02 _
 2.50e+02 _
 2.75e+02 _
 3.00e+02 _
 3.25e+02 _
 3.50e+02 _
 3.75e+02 _
 4.00e+02 _
 4.25e+02 _
 4.50e+02 _
 4.75e+02 _
 5.00e+02 _
 5.25e+02 _
 5.50e+02 _
 5.75e+02 _
 6.00e+02 _
 6.25e+02 _
 6.50e+02 _
 6.75e+02 _
 7.00e+02 _
 7.25e+02 _
 7.50e+02 _
 7.75e+02 _
 8.00e+02 _
 8.25e+02 _
 8.50e+02 _
 8.75e+02 _
 9.00e+02 _
 9.25e+02 _
 9.50e+02 _
 9.75e+02 _
 1.00e+03 _

real	63m38.282s
user	22m50.256s
sys	10m19.134s
```
