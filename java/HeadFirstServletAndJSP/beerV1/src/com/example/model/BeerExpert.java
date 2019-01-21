package com.example.model;

import java.util.*;

public class BeerExpert{
	public ArrayList<String> getBrands(String color){
		ArrayList<String> brands = new ArrayList<>();
		if(color.equals("amber")){
			brands.add("Jack Amber");
			brands.add("Red Moore");
		}
		else{
			brands.add("Jail pale ale");
			brands.add("Gout Stout");
		}
		return brands;
	}
}