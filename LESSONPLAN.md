# Lesson Plan

### Week 1 - Introduction to Molecular Dynamics

Computational chemistry is often used in undergraduate chemistry as a "black box". However, this it likely to reduce student engagement as while the application is clear, the unlying mechanics is not. The first week of the practical will be focused on refreshing material from the second year Introduction to computational chemistry CH20238 lecture module by allowing the students to interact directly with atomistic molecular dynamics simulations using the pylj software [1]. 

#### Learning Outcomes 

- Recognise the *recipe* associated with a molecular dynamics simulation.
- Understand the concepts of the Lennard-Jones potential and how it can be used in the modeling of atomic particles.
- Describe the Coulomb potential, and its importance in the modeling of ionic systems.
- Be able to build a molecular dynamics simulation, using the pylj framework. 
- Utilise the molecular dynamics simulation to study a system deviating from ideal gas behaviour. 

#### Lesson Plan

The will be a student led workshop where they will (in their own time) be able to work through an interactive Jupyter notebook that will detail the mechanism of atomistic simulation. At the end, the students will use the pylj framework to build a simple molecular dynamics simulation and use this to preform basic simulations. This will involve running simulations at a series of different atomistic densities to reflect on the effect of density on a *typical* ideal gas system.

##### Assesment 

- This week will form the basis for the methodology portion of the students report.
  
### Week 2 - Introduction to Transport Properties

The transport properties of a material are crucial for many technologies. These range from batteries/fuel cells to nuclear materials. Week 2 will take the knowledge of MD simulations learnt in week 1 and apply it to some real world examples. Students will run MD simulations on fluorite CaF<sub>2</sub> and analyse the transport properties of the material. 

#### Learning Outcomes 

- Mean Squared Displacement - Tutorial in Jupyter notebook
- Arhenius Equation - Tutorial in Jupyter notebook

#### Lesson Plan

- Run an intitial MD simulation on CaF<sub>2</sub> - Use this data to do MSD tutorial
- Run MD simulations on CaF<sub>2</sub> across a temperature range - Use data for Arhenius tutorial

#### Assesment 

- MSD / Arhenius theory will form part of the methodology of the students report
- The Arenius plot for CaF<sub>2</sub> will be required for the report   
  
### Week 3 - Defect Chemistry

No material is without defects. There are two main types of defect that exist in materials - Frenkel and Schottky defects. 
- Frenkel Defect = Interstitials 
- Schottky Defect = Missing formaula unit  

In week 3 students will introduce Frenkel and Schottky defects to the CaF<sub>2</sub> configuration from week 2. They will determine how these defects affect the tranpsort properties of the material. 
This will be the first week that does not include tutorials, the students will begin to use what they have learned in the first 2 weeks and begin to design their own simulations. 

#### Learning Outcomes

- Understand Frenkel and Schottky defects 

#### Lesson Plan

- Add cation Frenkel defects to CaF<sub>2</sub> and vary the concentration - How do Frenkel defects affect the transport properties
- Add Schottky defects to CaF<sub>2</sub> and vary the concentration - How do Schottky defects affect the transport properties. 

#### Assesment 

- Key Report Question - How do Frenkel/Schottky defects affect the transport properties? 
  
### Week 4 - Dopants 

It is now common practice to dope a material with different elements in order to improve a desired property. This is particularly common in fuel cell materials, eg Cerium oxide is doped with Gd<sup>3+</sup> cations in order to improve the oxygen transport(and conductivity) of the material - making it a better fuel cell material. In the final week students will investigate how dopant cations affect the transport properties of CaF<sub>2</sub>. Can they find a way to increase the diffusion coefficient?

#### Learning Outcomes

- How do you as a scientist alter the properties of a material?

#### Lesson Plan

- Select 4 - 5 cations and add them to CaF<sub>2</sub>. 

#### Assesment 

- Key Report Question - How do dopants affect the tranport properties.   
   
### Summary 

Over the 4 weeks the students will transition from a very hands on, teaching focused course to a hands off, research driven course. In weeks 1 and 2 the students will learn the underlying theory behind the practical course and how to carry out MD simulations. In weeks 3 and 4 the students will use this knowledge to design simulations to answer questions common to computational chemists. 

### References

1. McCluskey et al., (2018). pylj: A teaching tool for classical atomistic simulation . Journal of Open Source Education, 1(2), 19, https://doi.org/10.21105/jose.00019
