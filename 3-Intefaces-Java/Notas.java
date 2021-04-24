public class Notas implements Conceito{
  public String nomeALuno;
  public String conceitoAluno;

  Notas(String cAluno, String nome){
    this.nomeALuno = nome;
    this.conceitoAluno = cAluno;
  }
  @Override
  public String conceitos(){
    if (this.conceitoAluno == "a"){
     return "Parabéns, você atingiu todos os indicadores de avaliação com excelência";
    }
    else if(this.conceitoAluno == "b"){
      return "Parabéns, você obteve aproveitamento satisfatório nos indicadores de avaliação";
    }
    else{
      return "Você não atingiu o mínimo esperado para aprovação";
    }
  }
}