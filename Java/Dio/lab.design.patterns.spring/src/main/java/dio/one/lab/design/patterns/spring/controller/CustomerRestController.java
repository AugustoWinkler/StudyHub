package dio.one.lab.design.patterns.spring.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import dio.one.lab.design.patterns.spring.model.Customer;
import dio.one.lab.design.patterns.spring.service.CustomerService;

@RestController
@RequestMapping("customers")
public class CustomerRestController {

	@Autowired
	private CustomerService customerService;

	@GetMapping
	public ResponseEntity<Iterable<Customer>> findAll() {
		return ResponseEntity.ok(customerService.findAll());
	}

	@GetMapping("/{id}")
	public ResponseEntity<Customer> findById(@PathVariable Long id) {
		return ResponseEntity.ok(customerService.findCustomerById(id));
	}

	@PostMapping
	public ResponseEntity<Customer> add(@RequestBody Customer customer) {
		customerService.add(customer);
		return ResponseEntity.ok(customer);
	}

	@PutMapping("/{id}")
	public ResponseEntity<Customer> refresh(@PathVariable Long id, @RequestBody Customer customer) {
		customerService.refresh(id, customer);
		return ResponseEntity.ok(customer);
	}

	@DeleteMapping("/{id}")
	public ResponseEntity<Customer> delete(@PathVariable Long id) {
		customerService.delete(id);
		return ResponseEntity.ok(customerService.findCustomerById(id));
	}

}
