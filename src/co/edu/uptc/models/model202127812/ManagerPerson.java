package co.edu.uptc.models.model202127812;

import co.edu.uptc.pojos.Person;

import java.util.List;

public class ManagerPerson {
    private final ManagerModel202127812 managerModel;
    private final TreeUPTCPerson tree;

    public ManagerPerson(ManagerModel202127812 managerModel) {
        this.managerModel = managerModel;
        tree = new TreeUPTCPerson();
    }
    public void addPerson(Person person){
        if (person.getName().equals("") || person.getCode().equals("")) {
            managerModel.presenter.notifyError("Información incompleta");
        } else {
            tree.add(person);
            managerModel.presenter.notifyPeopleUpdated();
        }
    }
    public Person getPerson(String attribute){
        return tree.getPerson(attribute).clone();
    }
    public void editPerson(Person person){
        if (person.getName().equals("") || person.getCode().equals("")) {
            managerModel.presenter.notifyError("Información incompleta");
        } else {
            tree.editPerson(person);
            managerModel.presenter.notifyPeopleUpdated();
        }
    }
    public List<Person> getPeople(){
        return tree.getListFromTree();
    }
}
