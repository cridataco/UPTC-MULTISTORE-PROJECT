package co.edu.uptc.models.model202115100.myPojos;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class BinaryTree<T> {
    private NodeDouble<T> root;
    private Comparator<T> comparable;
    public BinaryTree(Comparator<T> comparable) {
        root = null;
        this.comparable = comparable;
    }

    public BinaryTree(T data) {
        root = new NodeDouble<>(data);
    }

    public NodeDouble<T> getRoot() {
        return root;
    }
    public void add(T data){
        root = addRecursive(root, data);
    }

    private NodeDouble<T> addRecursive(NodeDouble<T> current, T data) {
        if(current == null){
            return new NodeDouble<>(data);
        }
        if (comparable.compare(data, current.getData())<0) {
            current.setPrevious(addRecursive(current.getPrevious(), data));
        }
        if (comparable.compare(data, current.getData())>=0) {
            current.setNext(addRecursive(current.getNext(), data));
        }
        return current;
    }
    public void remove(T data){
        NodeDouble<T> nodeBehind = searchRecursive(root, data);
        removeRecursive(root, data);
    }

    private NodeDouble<T> searchRecursive(NodeDouble<T> root, T data) {
//pendiente
        return null;
    }

    private NodeDouble<T> removeRecursive(NodeDouble<T> current, T data) {
        return current;
    }
    public List<T> toList(NodeDouble<T> current) {
        List<T> list = new ArrayList<>();
        if (current != null) {
            list.addAll(toList(current.getPrevious()));
            list.add(current.getData());
            list.addAll(toList(current.getNext()));
        }
        return list;
    }

    public T search(NodeDouble<T> root, String attribute) {
        if (root == null) {
            return null;
        }
        if (root.getData().toString().toLowerCase().contains(attribute.toLowerCase())) {
            return root.getData();
        }
        T result = search(root.getPrevious(), attribute);
        if (result != null) {
            return result;
        }
        return search(root.getNext(), attribute);
    }
}