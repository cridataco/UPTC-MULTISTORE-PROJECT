package co.edu.uptc.models.model202127717;

import co.edu.uptc.pojos.Person;

import java.util.List;

public class ManagerPerson {
    private final ManagerModel202127717 managerModel;
    private final TreePerson treePerson;

    public ManagerPerson(ManagerModel202127717 managerModel) {
        this.managerModel = managerModel;
        treePerson = new TreePerson();
    }
    public void addPerson(Person person){
        if (person.getName().equals("") || person.getCode().equals("")) {
            managerModel.presenter.notifyError("Informacion incompleta");
        } else {
            treePerson.add(person);
            managerModel.presenter.notifyPeopleUpdated();
        }
    }

    public void editPerson(Person person){
        if (person.getName().equals("") || person.getCode().equals("")) {
            managerModel.presenter.notifyError("Información incompleta");
        } else {
            treePerson.editPerson(person);
            managerModel.presenter.notifyPeopleUpdated();
        }
    }
    public List<Person> getPeople(){
        return treePerson.getListFromTree();
    }

    public Person getPerson(String attribute){
        return treePerson.getPerson(attribute).clone();
    }
}
