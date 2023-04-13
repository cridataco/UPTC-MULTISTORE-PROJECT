package co.edu.uptc.models.model202127812;

import co.edu.uptc.pojos.Person;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class TreeUPTCPerson {
    private Node head;
    private Person toGet =null;
    private Person toEdit= null;
    private final Comparator<Person> comparator = Comparator.comparing(Person::getName);
    public void add(Person o){
        Node node = new Node(o);
        if (head==null){
            head=node;
        }else {
            Node temp = search(node);
            if (comparator.compare(o,temp.getInfo())>=0){
                temp.setMayorEqual(node);
            }else {
                temp.setMinor(node);
            }
        }
    }
    private Node search(Node node){
        Node aux =head;
        boolean isFounded = false;
        while (!isFounded){
            if (comparator.compare(node.getInfo(),aux.getInfo())<0){
                if (aux.getMinor()!=null){
                    aux = aux.getMinor();
                }else {
                    isFounded=true;
                }
            }else {
                if (aux.getMayorEqual()!=null){
                    aux=aux.getMayorEqual();
                }else {
                    isFounded=true;
                }
            }
        }
        return aux;
    }

    private Node search(Person value){
        if (head==null){
            return null;
        }
        Node aux =head;
        boolean isFounded = false;
        while (!isFounded){
            if (comparator.compare(value,aux.getInfo())<0){
                if (aux.getMinor()!=null){
                    aux = aux.getMinor();
                }else {
                    isFounded=true;
                }
            }else {
                if (comparator.compare(value,aux.getInfo())==0){
                    return aux;
                }
                if (aux.getMayorEqual()!=null){
                    aux=aux.getMayorEqual();
                }else {
                    isFounded=true;
                }
            }
        }
        return null;
    }
    public List<Person> getListFromTree(){
        List<Person> list= new ArrayList<>();
        if (head!=null){
            getTreePrev(head,list);
        }
        return list;
    }

    public void getTreePrev(Node node, List<Person> list){
        if (node.getMinor()!=null){
            getTreePrev(node.getMinor(),list);
        }
        list.add(node.getInfo().clone());
        if (node.getMayorEqual()!=null){
            getTreePrev(node.getMayorEqual(),list);
        }
    }
    public boolean remove(Person value){
        Node toRemove = search(value);
        if (toRemove!=null){
            Node toAdd;
            Node before = getBeforeTo(toRemove);
            if (before==null){
                toAdd = head.getMinor();
                head = head.getMayorEqual();
            }else {
                if (comparator.compare(before.getInfo(),toRemove.getInfo())<0){
                    toAdd = toRemove.getMinor();
                    before.setMayorEqual(toRemove.getMayorEqual());
                }else {
                    toAdd= toRemove.getMayorEqual();
                    before.setMinor(toRemove.getMinor());
                }
            }
            if (toAdd!=null){
                Node temp = search(toAdd);
                if (comparator.compare(toAdd.getInfo(),temp.getInfo())>=0){
                    temp.setMayorEqual(toAdd);
                }else {
                    temp.setMinor(toAdd);
                }
            }
            return true;
        }
        return false;
    }
    private Node getBeforeTo(Node node){
        if (comparator.compare(node.getInfo(),head.getInfo())==0){
            return null;
        }
        Node aux =head;
        boolean isFounded = false;
        while (!isFounded){
            if (comparator.compare(node.getInfo(),aux.getInfo())<0){
                if (aux.getMinor()!=null){
                    if (node.equals(aux.getMinor())){
                        return aux;
                    }else {
                        aux = aux.getMinor();
                    }
                }else {
                    isFounded=true;
                }
            }else {
                if (aux.getMayorEqual()!=null){
                    if (node.equals(aux.getMayorEqual())){
                        return aux;
                    }else {
                        aux=aux.getMayorEqual();
                    }
                }else {
                    isFounded=true;
                }
            }
        }
        return null;
    }
    public Person getPerson(String attribute){
        if (head!=null){
            putNodePersonToGet(head,attribute);
        }
        return toGet;
    }
    public void putNodePersonToGet(Node node, String attribute){
        if (node.getMinor()!=null){
            putNodePersonToGet(node.getMinor(),attribute);
        }
        if (node.getInfo().getName().equals(attribute)||node.getInfo().getCode().equals(attribute)){
            toGet =node.getInfo();
            return;
        }
        if (node.getMayorEqual()!=null){
            putNodePersonToGet(node.getMayorEqual(),attribute);
        }
    }
    public void editPerson(Person person){
        if (head!=null){
            putPersonToEdit(head,person.getId());
        }
        toEdit.setCode(person.getCode());
        toEdit.setName(person.getName());
    }

    private void putPersonToEdit(Node node, int idPerson) {
        if (node.getMinor()!=null){
            putPersonToEdit(node.getMinor(),idPerson);
        }
        if (node.getInfo().getId()==idPerson){
            toEdit =node.getInfo();
            return;
        }
        if (node.getMayorEqual()!=null){
            putPersonToEdit(node.getMayorEqual(),idPerson);
        }
    }
}
