package co.edu.uptc.models.model202113049;

import java.util.Comparator;

public class UPTCTree_202113049 <T>{

    Node_202113049<T> header;

    public void add(T info,Comparator<T> comparator,Comparator<T> comparator2) {
        Node_202113049 aux = new Node_202113049(info);
        if (header == null) {
            header = aux;
        } else {
            Node_202113049 tmp = search(aux,comparator);
            if (comparator2.compare(info, (T) tmp.getInfo())==0) {
                tmp.setMajorOrEqual(aux);
            }else {
                tmp.setLess(aux);
            }
        }
    }

    private Node_202113049 search(Node_202113049 node, Comparator<T> comparator){
        Node_202113049 aux = header;
        boolean isFound = false;
        while(isFound==false){
            if(comparator.compare((T) aux.getInfo(), (T) node.getInfo())==0){
                if(aux.getLess()!=null){
                    aux = aux.getLess();
                }else{
                    isFound = true;
                }
            }else{
                if(aux.getMajorOrEqual()!=null){
                    aux =aux.getMajorOrEqual();
                }else{
                    isFound = true;
                }
            }
        }
        return aux;
    }
}
