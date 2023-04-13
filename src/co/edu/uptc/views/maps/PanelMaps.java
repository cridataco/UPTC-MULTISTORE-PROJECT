package co.edu.uptc.views.maps;

import co.edu.uptc.views.Globals.ValuesGlobals;

import javax.swing.*;
import java.awt.*;

public class PanelMaps extends JPanel {

    public PanelMaps() {
        configGlobal();
        initializeComponents();
    }


    private void configGlobal(){
        setBackground(ValuesGlobals.COLOR_BACK_PANEL_WORK);
        setSize(new Dimension(1000,1000));
        setLayout(null);
    }

    private void initializeComponents() {
        addTitle();

    }

    private void addComponents(){

    }


    private void addTitle(){
        JLabel labelTitle = new JLabel("EN PROCESO DE IMPLEMENTACION");
        labelTitle.setFont(ValuesGlobals.FONT_H1);
        labelTitle.setBounds(10,40,1000,30);
        add(labelTitle);

    }


}
