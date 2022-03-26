# Threads Java Deitel

## Estados de uma Thread(Ciclos)
- Estados novo e executável;
    - Está no estado pronto
    - Aguardando o sistema despachar a thread.
- Estado de espera;
- Estado de espera sincronizada;
- Estado bloqueado;
- Estado terminado.

## Visão do Sistema Operacional e da JVM
A JVM não “vê” as transições (pronto e execução) — ela simplesmente vê a thread 
como executável e deixa para o sistema operacional fazer a transição entre a thread pronta e em execução.

Recomenda-se não criar e utilizar explicitamente objetos Thread para implementar a concorrência, mas, em vez disso, utilizar a interface Executor (que é descrita na Seção 23.3). A classe Thread contém alguns métodos static úteis, que utilizaremos mais adiante no capítulo.

# Criando e executando threads com o framework Executor
A interface Runnable declara o método run único, que contém o código que define a tarefa que um objeto
Runnable deve realizar.

- A interface Executor declara um único método chamado execute que aceita um Runnable como um argumento.

- O Executor atribui cada Runnable passado para o método execute a uma das threads disponíveis no pool de threads.

```
Não podemos prever a ordem em que as tarefas
começarão a ser executadas, mesmo se conhecermos a ordem em que elas foram criadas e iniciadas.
```

# Sincronização de thread
```
Quando várias threads compartilham um objeto e este é modificado por uma ou mais delas, podem ocorrer resultados indeterminados  a menos que o acesso ao objeto compartilhado (região crítica) seja gerenciado de forma adequada.
```
- Solução é a **exclusão mútua** garante que uma Thread por vez acesse a região crítica. 

## Monitores
- Cada objeto tem um monitor e um `bloqueio de monitor` (ou bloqueio intrínseco).

Para especificar que uma thread deve segurar um monitor de bloqueio para executar um bloco do código, o código deve ser colocado em uma instrução synchronized.
```java
synchronized (objeto)
{
 instruções
} 
```