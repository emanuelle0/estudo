public class CalculadoraAninhada{
  double num1;
  double num2;

CalculadoraAninhada(double a, double b){
  this.num1 = a;
  this.num2 = b;

}

class Soma{
  public double somar(){
    return num1 + num2;
  }
}

class Subtracao{
  public double subrair(){
    return num1 - num2;
  }
}

class Divisao{
  public double dividir(){
    return num1 / num2;
  }
}

class Multiplicacao{
  public double multiplicar(){
    return num1 * num2;
  }
}
}