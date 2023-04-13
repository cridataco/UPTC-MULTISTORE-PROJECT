package co.edu.uptc.views.people;

import co.edu.uptc.pojos.Person;
import co.edu.uptc.views.Globals.ValuesGlobals;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.JTableHeader;
import java.awt.*;
import java.util.List;

public class PanelInput extends JPanel {
    private JLabel labelCode;
    private JLabel labelName;
    private JLabel labelModel ;
    protected JTextField textFieldCode;
    protected JTextField textFieldName;
    protected  JTable jTable;
    private PanelPeople dialogPeople;

    public PanelInput(PanelPeople dialogPeople) {
        this.dialogPeople = dialogPeople;
        config();
        addComponents();
    }

    public void config() {

        setBackground(ValuesGlobals.COLOR_BACK_PANEL_WORK);
        setLayout(null);
    }

    private void addComponents() {
        addLabels();
        addTextFilds();
        addTable();

    }

    private void addLabels() {
        labelModel = new JLabel();
        updateAuthorModel();
        labelModel.setBounds(40, 10, 400, 25);
        add(labelModel);

        labelCode = new JLabel("Código");
        labelCode.setBounds(40, 40, 100, 25);
        labelName = new JLabel("Nombre");
        labelName.setBounds(40, 70, 100, 25);
        add(labelCode);
        add(labelName);
    }

    public void updateAuthorModel(){
       labelModel.setText("Author del modelo: "+dialogPeople.getAuthorOfModel());
    }


    private void addTextFilds() {
        textFieldCode = new JTextField();
        textFieldCode.setBounds(100, 40, 100, 25);
        textFieldName = new JTextField();
        textFieldName.setBounds(100, 70, 300, 25);
        add(textFieldCode);
        add(textFieldName);
    }


    private void addTable(){
        jTable = new JTable(0,2);
        JScrollPane scrollPane = new JScrollPane(jTable);
        scrollPane.setBounds(30,110,400,600);
        tableHeader(jTable.getTableHeader());
        add(scrollPane);
     //   loadPeople();
    }

    private void tableHeader(JTableHeader header) {
        header.getColumnModel().getColumn(0).setHeaderValue("Código") ;
        header.getColumnModel().getColumn(1).setHeaderValue("Nombre");
        header.setBorder(BorderFactory.createLineBorder(Color.black));
        header.setBackground(Color.yellow);
    }

    private void clearTable(){
        DefaultTableModel tableModel = (DefaultTableModel) jTable.getModel();
        tableModel.getDataVector().removeAllElements();
    }

    protected void loadPeople() {
        clearTable();
        DefaultTableModel tableModel = (DefaultTableModel) jTable.getModel();
        List<Person> auxList = dialogPeople.getPeople();
        if (auxList!=null) {
            if (!auxList.isEmpty()){
                for (Person person : auxList) {
                    tableModel.addRow(new Object[]{person.getCode(), person.getName()});
                }
            }else {
                tableModel.addRow(new Object[]{"",""});
            }
        } else {
            tableModel.addRow(new Object[]{"",""});
        }
        jTable.setModel(tableModel);
    }

    public Person getSelectedPerson(){
        int selectedRow = jTable.getSelectedRow();
        if (selectedRow != -1) {
            String value = (String)jTable.getValueAt(selectedRow, jTable.getSelectedColumn());
            return dialogPeople.getPerson(value);
        }
        return null;
    }

}
