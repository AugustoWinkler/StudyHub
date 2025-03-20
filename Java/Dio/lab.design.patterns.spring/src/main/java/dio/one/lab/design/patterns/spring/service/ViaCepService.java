package dio.one.lab.design.patterns.spring.service;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import dio.one.lab.design.patterns.spring.model.Adress;

@FeignClient(name = "viacep", url = "https://viacep.com.br/ws")
public interface ViaCepService {

	@RequestMapping(method = RequestMethod.GET, value = "/{cep}/json")
	Adress findCep(@PathVariable("cep") String cep);

}
