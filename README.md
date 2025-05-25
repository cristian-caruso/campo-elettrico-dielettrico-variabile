# Modi normali di un campo elettrico in un mezzo dielettrico

![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Made with](https://img.shields.io/badge/made%20with-Matplotlib-orange)
![Status](https://img.shields.io/badge/status-in%20development-yellow)

Questo progetto mostra come calcolare e visualizzare i modi normali di oscillazione di un campo elettrico lungo una dimensione, in presenza di un dielettrico con permittività variabile. L'analisi si basa sulla discretizzazione dell'operatore di Laplace ponderato e sulla risoluzione del problema agli autovalori.

## Descrizione

Viene simulato un dominio unidimensionale di lunghezza L = 1, diviso in N = 100 punti. La costante dielettrica relativa assume valori diversi in tre regioni:
- 1 per valori di *x* compresi tra 0.3 e 0.6
- 80 (come se ci fosse acqua) nelle due regioni adiacenti

L'operatore discreto viene rappresentato come una matrice tridiagonale simmetrica. Gli autovettori di questa matrice rappresentano i modi di oscillazione del campo elettrico.

## Documentazione

Per una descrizione dettagliata della teoria e dei metodi utilizzati, si veda il documento:

👉 [Spiegazione teorica.pdf](./Spiegazione_teorica.pdf)

## Output

L'output del programma corrisponde al grafico dei modi normali di oscillazione del campo elettrico. La zona in cui è presente il dielettrico è colorata di azzurro.

![Output](https://github.com/user-attachments/assets/bfd895a2-9c44-494e-934b-ba57569c32e1)

## Sviluppi futuri
In futuro, ho intenzione di estendere questo progetto a una superficie bidimensionale, in cui siano presenti regioni con differenti indici di rifrazione. Questo permetterà di analizzare fenomeni più complessi. Inoltre, ho intenzione di usare lo sviluppo in serie di Fourier per studiare la propagazione del campo elettrico nel tempo.

## Requisiti

- Python 3.x
- NumPy
- SciPy
- Matplotlib

Puoi installare i pacchetti necessari con:

```bash
pip install numpy
```
```bash
pip install scipy
```
```bash
pip install matplotlib
```

## Autore

Cristian Caruso

## Ringraziamenti e collaborazioni

Questo progetto è stato svolto con il supporto di un mio professore, che ringrazio per la disponibilità e i suggerimenti forniti.
