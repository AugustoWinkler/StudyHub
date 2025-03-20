package dio.one.lab.design.patterns.spring.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import dio.one.lab.design.patterns.spring.model.Customer;

@Repository
public interface CustomerRepository extends CrudRepository<Customer, Long> {

}
