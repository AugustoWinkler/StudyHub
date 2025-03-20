package dio.one.lab.design.patterns.spring.service;


import dio.one.lab.design.patterns.spring.model.Customer;

public interface CustomerService {

	Iterable<Customer> findAll();

	void add(Customer customer);

	void refresh(Long id, Customer customer);

	void delete(Long id);

	Customer findCustomerById(Long id);
}
