package co.edu.uptc.models.model202114641;

import co.edu.uptc.pojos.Person;

public class NodoArbol {
    private Person dato;
    private NodoArbol izquierdo;
    private NodoArbol derecho;

    public NodoArbol(Person dato) {
        this.dato = dato;
        izquierdo = null;
        derecho = null;
    }

    public Person getDato() {
        return dato;
    }

    public void setDato(Person dato) {
        this.dato = dato;
    }

    public NodoArbol getIzquierdo() {
        return izquierdo;
    }

    public void setIzquierdo(NodoArbol izquierdo) {
        this.izquierdo = izquierdo;
    }
    public NodoArbol getDerecho() {
        return derecho;
    }

    public void setDerecho(NodoArbol derecho) {
        this.derecho = derecho;
    }
}
