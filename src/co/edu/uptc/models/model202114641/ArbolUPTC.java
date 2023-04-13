package co.edu.uptc.models.model202114641;

import co.edu.uptc.pojos.Person;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class ArbolUPTC {

    private NodoArbol raiz;
    private int contador;
    List<Person> list;
private final Comparator<Person> comparator= Comparator.comparing(Person::getName);
    public ArbolUPTC() {
        list= new ArrayList<>();
        raiz = null;
        contador=0;
    }

    public void agregar(Person dato) {
        NodoArbol nuevoNodo = new NodoArbol(dato);
        if (raiz == null) {
            raiz = nuevoNodo;
        } else {
            agregarRecursivo(raiz, nuevoNodo);
        }
    }

    private void agregarRecursivo(NodoArbol actual, NodoArbol nuevoNodo) {
        if (comparator.compare(nuevoNodo.getDato(),actual.getDato())<0) {
            if (actual.getIzquierdo() == null) {
                actual.setIzquierdo(nuevoNodo);
            } else {
                agregarRecursivo(actual.getIzquierdo(), nuevoNodo);
            }
        } else {
            if (actual.getDerecho() == null) {
                actual.setDerecho(nuevoNodo);
            } else {
                agregarRecursivo(actual.getDerecho(), nuevoNodo);
            }
        }
    }

    public void recorrerInorden() {
        recorrerInorden(raiz);
    }
    public NodoArbol obtenerPorIndex(int index) {
        contador=0;
        return obtenerPorIndex(raiz, contador, index);
    }

    private NodoArbol obtenerPorIndex(NodoArbol actual, int contador, int index) {
        if (actual != null) {
            NodoArbol izquierdo = obtenerPorIndex(actual.getIzquierdo(), contador, index);
            if (izquierdo != null) {
                return izquierdo;
            }
            contador++;
            if (contador == index) {
                return actual;
            }
            NodoArbol derecho = obtenerPorIndex(actual.getDerecho(), contador, index);
            if (derecho != null) {
                return derecho;
            }
        }
        return null;
    }
    public List<Person> getList(){
    list= new ArrayList<>();
    recorrerInorden(raiz);
    return list;
    }
    private void recorrerInorden(NodoArbol actual) {

        if (actual != null) {
            recorrerInorden(actual.getIzquierdo());
            list.add(actual.getDato());
            recorrerInorden(actual.getDerecho());
        }
    }
}
