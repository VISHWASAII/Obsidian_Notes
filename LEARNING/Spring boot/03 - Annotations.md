```

@Controller - it indicates that the class responsibe for handling HTTP req

@RequestController - Controller + RequestBody -- it will handle JSON or XML

@ResponseBody - if we are using the controller then we need to use the the Response body the RequestController handle the response

@RequestParam - Used to bind request param to controller method parameter

@InitBinder - used to constomize before the data reaching to the endpoint

@PathVariable - Used to extract value from the Path url and help to bind to the controller method

@RequestBody - Bind the Body of HTTP request to controller method parameter

@ResponseEntity - used to Represent the HTTP response.
```