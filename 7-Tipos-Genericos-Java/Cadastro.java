public class Cadastro<E>{
  E nome;
  E sobrenome;
  E idade;
  E endereco;
  E email;

  Cadastro(E n, E s, E i, E e, E em){
    nome = n;
    sobrenome = s;
    idade = i;
    endereco = e;
    email = em;
  }

  public void imprime(){
    System.out.println("Nome: " + nome + " " + sobrenome + "\nIdade: " + idade+"\nEndereço: " + endereco +"\nE-mail: "+ email);
  }


}