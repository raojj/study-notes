package com.joe.User.controller;

import com.joe.User.entity.User;
import com.joe.User.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/user")
@CrossOrigin(origins = "*", maxAge = 3600)
public class UserController {

    @Autowired
    UserRepository repo;

    @PostMapping
    User save(@RequestBody User user) {
        return repo.save(user);
    }

    @GetMapping
    List<User> userList() {
        return repo.findAll();
    }

    @DeleteMapping("/{id}")
    void delete(@PathVariable int id) {
        repo.deleteById(id);
    }
}
