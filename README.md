# AccuKnox Django Trainee Assignment

## Repository

This repository contains solutions for the AccuKnox Django Trainee Assignment.

---

## Question 1: Are Django Signals Synchronous by Default?

### Answer

Yes. Django signals execute synchronously by default.

### Proof

A `post_save` signal handler was created with a 5-second delay using `time.sleep(5)`.

The HTTP response was delayed by approximately 5 seconds before returning.

### Observation

Browser Output:

```text
Time Taken: 5.04 seconds
```

### Conclusion

The request waited for the signal handler to complete before returning a response. Therefore, Django signals are synchronous by default.

---

## Question 2: Do Django Signals Run in the Same Thread as the Caller?

### Answer

Yes. Django signals run in the same thread as the caller by default.

### Proof

The thread ID was printed from both the view and the signal handler using:

```python
threading.get_ident()
```

### Observation

```text
Caller Thread: 23192
Signal Thread: 23192
```

### Conclusion

Both thread IDs are identical, proving that the signal handler executes in the same thread as the caller.

---

## Question 3: Do Django Signals Run in the Same Database Transaction as the Caller?

### Answer

Yes. Django signals run in the same database transaction as the caller by default.

### Proof

An Employee record was created inside a `transaction.atomic()` block.

A signal handler created an Audit record.

An exception was raised to force a rollback.

### Observation

After rollback:

```text
Employees = 0
Audits = 0
```

### Conclusion

Both records were rolled back together, proving that the signal handler participated in the same database transaction.

---

## Rectangle Class

### Requirements

* Rectangle requires `length` and `width`.
* Rectangle is iterable.
* Iteration returns:

  * `{'length': value}`
  * `{'width': value}`

### Example

```python
rectangle = Rectangle(10, 5)

for item in rectangle:
    print(item)
```

### Output

```text
{'length': 10}
{'width': 5}
```

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```
