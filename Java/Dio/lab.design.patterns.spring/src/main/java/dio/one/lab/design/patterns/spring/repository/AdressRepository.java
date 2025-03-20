package dio.one.lab.design.patterns.spring.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import dio.one.lab.design.patterns.spring.model.Adress;

@Repository
public interface AdressRepository extends CrudRepository<Adress, String> {

}
