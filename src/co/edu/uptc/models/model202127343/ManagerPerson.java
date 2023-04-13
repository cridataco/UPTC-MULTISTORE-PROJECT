package co.edu.uptc.models.model202127343;

import co.edu.uptc.pojos.Person;

import java.util.List;

public class ManagerPerson {

   private TreeList treeList;
    private ManagerModel202127343 managerGeneral;

    public ManagerPerson(ManagerModel202127343 managerGeneral) {
        this.managerGeneral = managerGeneral;
        treeList = new TreeList();
    }

    public void addPerson(Person person){
        if (person.getName().equals("") || person.getCode().equals("")) {
           managerGeneral.presenter.notifyError("Información incompleta");
        } else {
            treeList.add(person);
            managerGeneral.presenter.notifyPeopleUpdated();
        }
   }

   public Person getPerson(String attribute){
       return null;
   }

   public void editPerson(Person person){
   }

    public List<Person> getPeople() {
        return treeList.getPersonArrayOfTree();
    }
}
