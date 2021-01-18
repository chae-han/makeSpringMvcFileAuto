
@Slf4j
@AllArgsConstructor
@RequestMapping("/v{number:[1,2]}/testname/")
@RestController
public class TestnameController {

    private TestnameService testnameService;

	List<ResponseModel> testFunction(int count, RequestModel requestModel){

		return new Object();

	}

	List<ResponseModel> test2Function(int count, RequestModel requestModel){

		return new Object();

	}



}