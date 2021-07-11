import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
import {Router} from '@angular/router';
import { ActivatedRoute } from '@angular/router';
import {Emitters} from '../emitters/emitters';

@Component({
  selector: 'app-restaurant',
  templateUrl: './restaurant.component.html',
  styleUrls: ['./restaurant.component.css']
})
export class RestaurantComponent implements OnInit {


  id:any = "";
  restaurant:any = "";

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private _Activatedroute:ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.id = this._Activatedroute.snapshot.paramMap.get("id");
    console.log("this.id--",this.id);
    this.get_resaturant_details(this.id);
  }

  get_resaturant_details(id:any){

      console.log("called---");
      this.http.get('http://localhost:8000/api/restaurants/' + id, {}).subscribe(
      (response: any)  => {
        console.log(typeof response);
        console.log(response);
        this.restaurant = response;
        // Emitters.authEmitter.emit(true);
      },
      err => {
        // Emitters.authEmitter.emit(true);
        // this.message = "You are not logged in";
        // Emitters.authEmitter.emit(false);
      }
    );

    }

}
