package co.edu.uptc.models.model202128687;
public class TreeSearch {
    Node header;

    public TreeSearch(){

    }

    public void add(int info) {
        Node aux = new Node(info);
        if (header == null) {
            header = aux;
        } else {
            Node tmp = search(aux);
            if (info >= tmp.getInfo()) {
                tmp.setMajorAndEqual(aux);
                aux.setNodeFather(tmp);
            } else {
                tmp.setLess(aux);
                aux.setNodeFather(tmp);
            }
        }
    }

    private Node search(Node node) {
        Node aux = header;
        boolean found = false;
        while (!found) {
            if (aux.getInfo() >= node.getInfo()) {
                if (aux.getLess() == null) {
                    aux.setLess(node);
                } else {
                    found = true;
                }
            } else {
                if (aux.getMajorAndEqual() != null) {
                    aux = aux.getMajorAndEqual();
                } else {
                    found = true;
                }
            }
        }
        return aux;
    }

    public void showTree() {
        if (header == null) {
            System.out.println("El arbol esta vacio");
        } else {
            showTreeOrder(header);
        }
    }

    public void showTreeOrder(Node node) {
        //System.out.println(node.getInfo());
        if (node.getLess() != null) {
            showTreeOrder(node.getLess());
        }
        System.out.println(node.getInfo());
        if (node.getMajorAndEqual() != null) {
            showTreeOrder(node.getMajorAndEqual());
        }
        //System.out.println(node.getInfo());
    }

    private Node getFather(Node node) {
        return search(node).getNode().getNodeFather();
    }

    private Node getLess(Node node) {
        return search(node).getLess();
    }

    private Node getMajorAndEqual(Node node) {
        return search(node).getMajorAndEqual();
    }

    private Node getToDelete(Node node) {
        return search(node);
    }

    public void delete(int info) {
        Node nodeToDelete = getToDelete(new Node(info));
        Node nodeFather = getFather(nodeToDelete);
        if (getLess(nodeToDelete) == null && getMajorAndEqual(nodeToDelete) == null) {
            System.out.println("si el nodo no tiene hijos");
            getFather(nodeToDelete).setLess(null);
        } else if (getLess(nodeToDelete) != null && getMajorAndEqual(nodeToDelete) == null) {
            System.out.println("si el nodo tiene un hijo menor");
            nodeFather.setLess(getLess(nodeToDelete));
        } else if (getLess(nodeToDelete) == null && getMajorAndEqual(nodeToDelete) != null) {
            System.out.println("si el nodo tiene un hijo mayor");
            nodeFather.setMajorAndEqual(getMajorAndEqual(nodeFather));
        } else {
            System.out.println("si el nodo tiene dos hijos");
            nodeToDelete.setInfo(getLastLeftChild(nodeToDelete).getInfo());
        }
    }

    private Node getLastLeftChild(Node father){
        Node aux = father;
        while (aux.getLess() != null){
            aux = aux.getLess();
        }
        father = aux.getNodeFather();
        father.setLess(null);
        return aux;
    }
}
