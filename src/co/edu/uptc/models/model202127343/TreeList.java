package co.edu.uptc.models.model202127343;

import co.edu.uptc.pojos.Person;

import java.util.ArrayList;
import java.util.List;

public class TreeList {

    private Node<Person> header;
    private MyComparator myComparator;

    public TreeList() {
        myComparator = new MyComparator();
    }

    public void add(Person person) {
        Node<Person> aux = new Node<Person>(person);
        if (header == null) {
            header = aux;
        } else {
            Node<Person> tmp = search(aux);
            int tmpComparate = myComparator.personComparetor(aux.getInfo(), tmp.getInfo());
            if (tmpComparate == 0 || tmpComparate == 1)
                tmp.setMajorAndEqual(aux);
            else {
                tmp.setLess(aux);
            }
        }
    }

    public List<Person> getPersonArrayOfTree() {
        if(header == null){
            return null;
        } else {
            return getArrayThreePerOrden(header);
        }
    }

    public List<Person> getArrayThreePerOrden(Node<Person> node) {
        List<Person> auxList = new ArrayList<>();
        if(node != null){
            auxList.addAll(getArrayThreePerOrden(node.getLess()));
            auxList.add(node.getInfo());
            auxList.addAll(getArrayThreePerOrden(node.getMajorAndEqual()));
        }
        return auxList;
    }

    public Node search(Node<Person> node) {
        Node<Person> aux = header;
        boolean found = false;
        while (!found) {
            if (myComparator.personComparetor(aux.getInfo(), node.getInfo()) == 1) {
                if (aux.getLess() != null) {
                    aux = aux.getLess();
                } else {
                    found = true;
                }
            } else {
                if (aux.getMajorAndEqual() != null)
                    aux = aux.getMajorAndEqual();
                else {
                    found = true;
                }
            }
        }
        return aux;
    }

    public void deleteNode(int info){
        Node<Person> tmp = new Node(info);
        Node<Person> aux = search(tmp);
    }
}
