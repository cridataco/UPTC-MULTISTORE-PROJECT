package co.edu.uptc.models.model202128687;

// Vamos a usar arboles binarios de busqueda
public class Node {
    private int info;
    private Node less = null;
    private Node majorAndEqual = null;
    private Node nodeFather;

    public Node(){

    }
    public Node(int info,Node less, Node majorAndEqual){
        this.info = info;
        this.less = less;
        this.majorAndEqual = majorAndEqual;
    }

    public Node(int info){
        this.info = info;
    }

    public int getInfo() {
        return info;
    }

    public void setInfo(int info) {
        this.info = info;
    }

    public Node getLess() {
        return less;
    }

    public void setLess(Node less) {
        this.less = less;
    }

    public Node getMajorAndEqual() {
        return majorAndEqual;
    }

    public void setMajorAndEqual(Node majorAndEqual) {
        this.majorAndEqual = majorAndEqual;
    }

    public Node getNodeFather() {
        return nodeFather;
    }

    public void setNodeFather(Node nodeFather) {
        this.nodeFather = nodeFather;
    }

    public Node getNode(){
        return this;
    }

    @Override
    public String toString() {
        return "Node [info=" + info + ", less=" + less + ", majorAndEqual=" + majorAndEqual + "]";
    }
}
