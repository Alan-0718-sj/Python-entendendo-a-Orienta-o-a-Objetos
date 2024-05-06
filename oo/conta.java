// class Conta {

//     //atributos
//     private int numero;
//     private String titular;
//     private double saldo;
//     private double limite;

//     //construtor
//     Conta(int numero, String titular, double saldo, double limite) {
//         this.numero = numero;
//         this.titular = titular;
//         this.saldo = saldo;
//         this.limite = limite;
//     }


//     //metodos
//     void extrato() {
//         System.out.println("Saldo de " + this.saldo + "")
//     }

//     void deposita(double valor) {
//         this.saldo += valor;
//     }


//     public double getLimite() {
//         return limite;
//     }

//     public void setLimite(double limite) {
//         this.limite = limite;
//     }

//     public double getNumero() {
//         return numero;
//     }

//     public void getTitular() {
//         return titular;
//     }

//     public double getSaldo() {
//         return saldo;
//     }

// }


// Conta contaDoNico = new Conta(123, "Nico", 55.5, 1000.0); contaDoNico.deposita(100.0);

// import java.util.Scanner;

// public class ContaInicial {
//     public static void main(String[] args) {

//         Scanner entrada = new Scanner(System.in);

//         System.out.println("""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
//         Dados iniciais do Cliente:
//             Nome:               Matteus Guimarães Moreno
//             Tipo da Conta:      Conta Corrente
//             Saldo inicial:      R$2500,00
//             """);

//         String nome = "Matteus Guimarães Moreno";
//         double saldoInicial = 2500.00;

//         while (true){
//             System.out.println("""
//                     =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
//                     Operações:
                    
//                     [1] Consultar Saldo
//                     [2] Receber Valor
//                     [3] Transferir Valor
//                     [4] Sair
//                     """);
//             System.out.print("Digite a opção desejada: ");
//             int opcao = entrada.nextInt();

//             if (opcao == 1){
//                 System.out.printf("O Saldo atual do correntista %s é: R$%.2f%n", nome, saldoInicial);
//             } else if (opcao == 2){
//                 System.out.print("Valor que deseja receber: R$");
//                 double valorRecebido = entrada.nextDouble();
//                 if (valorRecebido < 0){
//                     System.out.println("Não é possível transferir valor menor que 0");
//                 }else {
//                     saldoInicial += valorRecebido;
//                 }
//             }
//             else if (opcao == 3){
//                 System.out.print("Valor que deseja transferir: R$");
//                 double valorTransferido = entrada.nextDouble();
//                 if (valorTransferido > saldoInicial){
//                     System.out.println("Você não tem saldo suficiente");
//                 }else {
//                     saldoInicial -= valorTransferido;
//                 }
//             } else if (opcao == 4) {
//                 break;
//             } else {
//                 System.out.println("Opção Inválida. Tente novamente !");
//             }
//         }
//     }
// }
