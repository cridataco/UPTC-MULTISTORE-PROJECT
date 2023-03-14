package co.edu.uptc.views.people;

import co.edu.uptc.pojos.Person;
import co.edu.uptc.views.dashBoard.DashBoard;

import javax.swing.*;
import java.awt.*;
import java.util.List;


public class DialogPeople extends JDialog {
    private DashBoard dashBoard;

    private PanelButtom panelButtom;

    private PanelInput panelInput;
    public DialogPeople(DashBoard dashBoard)  {
        super(dashBoard,true);
        this.dashBoard = dashBoard;
        setSize(new Dimension(500 ,500));
        setLocationRelativeTo(dashBoard);
        addComponents();
    }

    private void addComponents(){
        panelButtom = new PanelButtom(this);
        add(panelButtom, BorderLayout.SOUTH);
        panelInput = new PanelInput(this);
        add(panelInput,BorderLayout.CENTER);
    }

    public void close(){
        this.setVisible(false);
    }


    public Person getPerson(){
        Person person = new Person();
        person.setCode(panelInput.textFieldCode.getText());
        person.setName(panelInput.textFieldName.getText());
        return  person;
    }

    public void addPerson(){
        Person p = getPerson();
        dashBoard.addPerson(p);
    }

    public void updatedPerson(){
        panelInput.loadPeople();
    }

    public List<Person> getPeople(){
        return dashBoard.getPeople();
    }

}
