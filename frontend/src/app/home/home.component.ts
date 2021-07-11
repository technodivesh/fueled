import { Component,NgModule, OnInit, EventEmitter } from '@angular/core';
import {HttpClient , HttpHeaders, HttpParams} from '@angular/common/http';
import {Emitters} from '../emitters/emitters';
import { Pipe, PipeTransform } from '@angular/core';


interface Student {
    id: Number;
    name: String;
    email: String;
    gender: String;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  // encapsulation: ViewEncapsulation.ShadowDom,
})
export class HomeComponent implements OnInit {
  message = "You are not logged in";
  restaurants:any = [];
  authenticated = false;
  // get_resaturant_list: any = "";

  constructor(
    private http: HttpClient
    ) { }

  ngOnInit(): void {

    Emitters.authEmitter.subscribe(
      (auth: boolean) => {
        this.authenticated = auth;
      }
    );
    this.http.get('http://localhost:8000/api/user', {withCredentials: true}).subscribe(
      (res: any)  => {
        console.log(res);
        this.message = `Hi ${res.username}`;
        localStorage.setItem('username', `${res.username}`);
        localStorage.setItem('id', `${res.id}`);
        Emitters.authEmitter.emit(true);
      },
      err => {
        this.message = "You are not logged in";
        Emitters.authEmitter.emit(false);
      }
    );
    this.get_resaturant_list(false);
    //////////////////
    
  }
    //////////////////

    get_resaturant_list(all:any){
      // const headers = new HttpHeaders().append('header', 'value');
      const params = new HttpParams().append('all', all);

      this.http.get('http://localhost:8000/api/restaurants/', {params}).subscribe(
      (response: any)  => {
        console.log(typeof response);
        console.log(response);
        this.restaurants = response;
      },
      err => {
        // this.message = "You are not logged in";
        // Emitters.authEmitter.emit(false);
      }
    );

    }

    // this.form.getRawValue()
    thumbdowns(restaurant:any){

      console.log("ThumbsDown",restaurant);
      alert("Are you sure to ThumbsDown this restaurant");

      this.http.post('http://localhost:8000/api/thumbdowns/', {user:9,restaurant:restaurant.id}, 
        {withCredentials: true}
      ).subscribe();
      this.restaurants.splice(restaurant,1);

    }
    //////////////////

}
