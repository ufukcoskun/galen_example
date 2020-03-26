package com.galenframework.java.sample.tests;

import com.galenframework.java.sample.components.GalenTestBase;
import com.galenframework.java.sample.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class CheckoutSmokeTest extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void cartPage(TestDevice device) throws IOException {
        load("/ayagina-gelsin/sepetim");
        checkLayout("/specs/cartPage.spec", device.getTags());
    }

}
