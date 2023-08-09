# Final Project: HR System

English | [Português](README_pt-br.md) 

This is the final project for the module. The goal is to create an HR system that meets the specified requirements below.

## Requirements

The system should be able to store employee records, including name, last name, phone number, profession, and date of birth.

System functionalities:

- `Create`: Allow adding new records to the system.
- `Read`: Retrieve complete records by searching for name or profession. The name should be displayed with the first letters capitalized, and the phone number should be in the format "(dd) 1234-5678". The data should be presented in a visually pleasing manner.
- `Update`: Allow updating a record by searching for the phone number.
- `Delete`: Allow deleting a record by searching for the phone number.

Each operation should be implemented in its own function. It should be possible to call a single function called `menu()` that allows the user to access the different operations.

## Bonus

- **Bonus 1**: When performing the read operation, display the number of days remaining until the registered employee's birthday.
- **Bonus 2**: Receive the employee's ZIP code and store the corresponding address.

## License

This project is licensed under the [MIT License](LICENSE).
