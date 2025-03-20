package dio.one.lab.design.patterns.spring.service;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import dio.one.lab.design.patterns.spring.model.Adress;
import dio.one.lab.design.patterns.spring.model.Customer;
import dio.one.lab.design.patterns.spring.repository.AdressRepository;
import dio.one.lab.design.patterns.spring.repository.CustomerRepository;

@Service
public class ClienteServiceImpl implements CustomerService {

	@Autowired
	private AdressRepository adressRepository;

	@Autowired
	private CustomerRepository customerRepository;

	@Autowired
	private ViaCepService viaCepService;

	@Override
	public Iterable<Customer> findAll() {
		return customerRepository.findAll();
	}

	@Override
	public Customer findCustomerById(Long id) {
		Optional<Customer> customer = customerRepository.findById(id);
		return customer.get();
	}

	@Override
	public void add(Customer customer) {
		saveCustomerByCep(customer);
	}

	@Override
	public void refresh(Long id, Customer customer) {
		Optional<Customer> customerBD = customerRepository.findById(id);
		if (customerBD.isPresent()) {
			saveCustomerByCep(customer);
		}
	}

	@Override
	public void delete(Long id) {
		customerRepository.deleteById(id);
	}

	private void saveCustomerByCep(Customer customer) {
		String cep = customer.getAdress().getCep();
		Adress adress = adressRepository.findById(cep).orElseGet(() -> {
			Adress newAdress = viaCepService.findCep(cep);
			adressRepository.save(newAdress);
			return newAdress;
		});
		customer.setAdress(adress);
		customerRepository.save(customer);
	}

}
