public class Area{

  public double calcularArea(double lado){//Cálculo área do quadrado.
    return lado * lado;
  }


public double calcularArea(double base, double altura){//Cálculo da área do retângulo.
  return base * altura;
}

public double calcularArea(double baseMax, double baseMin, double altura){//Cálculo da área do trapézio.
  return ((baseMax + baseMin)* altura)/2;
}
}