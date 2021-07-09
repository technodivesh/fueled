import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {HttpClient} from '@angular/common/http';
import {Router} from '@angular/router';

@Component({
  selector: 'app-restaurant',
  templateUrl: './restaurant.component.html',
  styleUrls: ['./restaurant.component.css']
})
export class RestaurantComponent implements OnInit {

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router
  ) { }

  ngOnInit(): void {
    // this.form = this.formBuilder.group({
    //   username: '',
    //   email: '',
    //   password: ''
    // });

  }

  // submit(): void {
  //   console.log(this.form.getRawValue())
  //   this.http.post('http://localhost:8000/api/signup/', this.form.getRawValue())
  //     .subscribe(() => this.router.navigate(['/login']));
  // }

}
