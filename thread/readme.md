## Métodos utilizados em Threads

- `start()` inicializa uma Thread;

- `sleep(TIME)` Faz com que a thread fique suspensa durante um eterminado tempo _(Passa de rodando para BLOQUEADA)_

- `wait()` faz com que a thread fique suspensa até que seja explicitamente reativada (notificado) poruma outra thread usando os métodos `notify()` ou `notifyAll()`

- `yield()` - Faz com que a execução da thread corrente seja suspensa para que uma outra thread seja escalonada _(executado)_

- `join()` 

```java
// Só executa o o print após o fim das duas threads
a.join();
b.join();
    
System.out.println("Fim do Main");
```
